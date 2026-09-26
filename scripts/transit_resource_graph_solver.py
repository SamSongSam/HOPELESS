#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
================================================================================
ISTRORIGAN TRANSIT & RESOURCE FLOW GRAPH SOLVER (YEAR 4205)
================================================================================
Implements 04_PCG_PIPELINE/03_TRANSIT_AND_RESOURCE_GRAPH.md:
- Layer 1: High-Speed Maglev Rail (Spines along v=0, Core Terminal, Ring Bridges)
- Layer 2: Utility & Life Support Trunks (O2, Desalination Freshwater, Geothermal Power)
- Layer 3: Pedestrian Walkways & Evacuation Tubes to Citadel Bunker
- Disaster Isolation Simulation: Dijkstra shortest-path rerouting around breached nodes
================================================================================
Usage:
    py scripts/transit_resource_graph_solver.py
Outputs:
    output/istrorigan_transit_graph.json
    output/istrorigan_transit_graph.csv
================================================================================
"""

# region MODULE IMPORTS
import os
import sys
import math
import json
import csv
import heapq
# endregion

# region GRAPH DATA STRUCTURES

class CityNode:
    def __init__(self, node_id, name, layer, node_type, petal_idx, x, y, z, capacity=1000.0):
        self.node_id = node_id
        self.name = name
        self.layer = layer              # "Transit_Maglev", "Utility_Trunk", "Pedestrian_Evac"
        self.node_type = node_type      # "Station", "PowerSubstation", "O2Terminal", "EvacBunker"
        self.petal_idx = petal_idx      # 0..7 or -1 for Core
        self.x = x
        self.y = y
        self.z = z
        self.capacity = capacity
        self.is_operational = True
        self.edges = []                 # List of (neighbor_id, edge_id, weight)

    def to_dict(self):
        return {
            "node_id": self.node_id,
            "name": self.name,
            "layer": self.layer,
            "node_type": self.node_type,
            "petal_idx": self.petal_idx,
            "x": round(self.x, 2),
            "y": round(self.y, 2),
            "z": round(self.z, 2),
            "capacity": self.capacity,
            "is_operational": self.is_operational
        }


class CityEdge:
    def __init__(self, edge_id, start_node, end_node, edge_type, distance, max_throughput=500.0):
        self.edge_id = edge_id
        self.start_node = start_node
        self.end_node = end_node
        self.edge_type = edge_type      # "MaglevRail", "PowerConduit", "OxygenPipe", "SkywalkTube"
        self.distance = distance
        self.max_throughput = max_throughput
        self.is_sealed = False          # Bulkhead status

    def to_dict(self):
        return {
            "edge_id": self.edge_id,
            "start_node": self.start_node,
            "end_node": self.end_node,
            "edge_type": self.edge_type,
            "distance_m": round(self.distance, 2),
            "max_throughput": self.max_throughput,
            "is_sealed": self.is_sealed
        }

# endregion

# region GRAPH GENERATOR

class IstroriganGraphBuilder:
    def __init__(self, petal_count=8, base_r_cm=15000.0, petal_len_cm=95000.0):
        self.petal_count = petal_count
        self.base_r_cm = base_r_cm
        self.petal_len_cm = petal_len_cm
        self.nodes = {}
        self.edges = {}
        self.next_node_id = 100
        self.next_edge_id = 1000

    def add_node(self, name, layer, node_type, petal_idx, x_cm, y_cm, z_cm, capacity=1000.0):
        nid = self.next_node_id
        self.next_node_id += 1
        node = CityNode(nid, name, layer, node_type, petal_idx, x_cm, y_cm, z_cm, capacity)
        self.nodes[nid] = node
        return nid

    def add_edge(self, start_id, end_id, edge_type, max_throughput=500.0):
        n1 = self.nodes[start_id]
        n2 = self.nodes[end_id]
        dist_cm = math.sqrt((n1.x - n2.x)**2 + (n1.y - n2.y)**2 + (n1.z - n2.z)**2)
        eid = self.next_edge_id
        self.next_edge_id += 1
        edge = CityEdge(eid, start_id, end_id, edge_type, dist_cm, max_throughput)
        self.edges[eid] = edge
        n1.edges.append((end_id, eid, dist_cm))
        n2.edges.append((start_id, eid, dist_cm))
        return eid

    def build_complete_network(self):
        print("[*] Constructing Multi-Layer Transit & Resource Graph (Centimeters)...")

        # -------------------------------------------------------------
        # CORE CENTRAL HUBS (cm)
        # -------------------------------------------------------------
        core_maglev = self.add_node("Core Central Maglev Terminal", "Transit_Maglev", "Station", -1, 0.0, 0.0, 1500.0, 50000.0)
        core_power = self.add_node("Core Geothermal Reactor Bus", "Utility_Trunk", "PowerSubstation", -1, 0.0, 0.0, -10000.0, 100000.0)
        core_o2 = self.add_node("Core Oxygen & Desalination Main", "Utility_Trunk", "O2Terminal", -1, 0.0, 0.0, 2500.0, 80000.0)
        core_bunker = self.add_node("Citadel Sovereign Emergency Bunker", "Pedestrian_Evac", "EvacBunker", -1, 0.0, 0.0, 20000.0, 100000.0)

        inter_petal_maglev_ring2 = []
        inter_petal_maglev_ring3 = []

        # -------------------------------------------------------------
        # BUILD 8 PETAL SPINES & UTILITIES (cm)
        # -------------------------------------------------------------
        for p in range(self.petal_count):
            ang_deg = p * (360.0 / self.petal_count)
            ang_rad = math.radians(ang_deg)
            cos_a, sin_a = math.cos(ang_rad), math.sin(ang_rad)

            # Stations along longitudinal spine (u = 0.2, 0.5, 0.85)
            u_stops = [0.20, 0.50, 0.85]
            maglev_stops = []
            power_stops = []
            evac_stops = []

            for u in u_stops:
                r_cm = self.base_r_cm + (u * self.petal_len_cm)
                x = r_cm * cos_a
                y = r_cm * sin_a
                z = 1000.0 if u > 0.70 else 2200.0

                # Layer 1: Maglev Station
                m_nid = self.add_node(f"Petal {p+1} Maglev Stn (u={u})", "Transit_Maglev", "Station", p, x, y, z, 5000.0)
                maglev_stops.append(m_nid)

                # Layer 2: Power / O2 Terminal
                pw_nid = self.add_node(f"Petal {p+1} Power Bus (u={u})", "Utility_Trunk", "PowerSubstation", p, x + 2000*cos_a, y + 2000*sin_a, z - 800.0, 12000.0)
                power_stops.append(pw_nid)

                # Layer 3: Pedestrian / Evac Dome Station
                ev_nid = self.add_node(f"Petal {p+1} Evac Shelter (u={u})", "Pedestrian_Evac", "EvacBunker", p, x - 2000*cos_a, y - 2000*sin_a, z + 500.0, 8000.0)
                evac_stops.append(ev_nid)

            # Connect Maglev Spine: Core -> Stop0 -> Stop1 -> Stop2
            self.add_edge(core_maglev, maglev_stops[0], "MaglevRail", 8000.0)
            self.add_edge(maglev_stops[0], maglev_stops[1], "MaglevRail", 6000.0)
            self.add_edge(maglev_stops[1], maglev_stops[2], "MaglevRail", 4000.0)

            # Connect Power Bus: Core -> Stop0 -> Stop1 -> Stop2
            self.add_edge(core_power, power_stops[0], "PowerConduit", 20000.0)
            self.add_edge(power_stops[0], power_stops[1], "PowerConduit", 15000.0)
            self.add_edge(power_stops[1], power_stops[2], "PowerConduit", 10000.0)

            # Connect Evac Spine: Stop2 -> Stop1 -> Stop0 -> Core Citadel Bunker
            self.add_edge(evac_stops[2], evac_stops[1], "SkywalkTube", 3000.0)
            self.add_edge(evac_stops[1], evac_stops[0], "SkywalkTube", 4000.0)
            self.add_edge(evac_stops[0], core_bunker, "SkywalkTube", 10000.0)

            # Local cross-connections between stops on same petal
            for i in range(len(u_stops)):
                self.add_edge(maglev_stops[i], evac_stops[i], "SkywalkTube", 2000.0)
                self.add_edge(power_stops[i], maglev_stops[i], "PowerConduit", 5000.0)

            # Store for inter-petal bridges
            inter_petal_maglev_ring2.append(maglev_stops[1])
            inter_petal_maglev_ring3.append(maglev_stops[2])

        # -------------------------------------------------------------
        # INTER-PETAL RING MONORAIL BRIDGES (Cross-waterway Ring 2 & 3)
        # -------------------------------------------------------------
        for p in range(self.petal_count):
            next_p = (p + 1) % self.petal_count
            # Ring 2 Monorail Bridge across 45m waterway
            self.add_edge(inter_petal_maglev_ring2[p], inter_petal_maglev_ring2[next_p], "MaglevRail", 4500.0)
            # Ring 3 Perimeter Harbor Bridge
            self.add_edge(inter_petal_maglev_ring3[p], inter_petal_maglev_ring3[next_p], "MaglevRail", 3000.0)

        print(f"[+] Multi-Layer Graph built: {len(self.nodes)} Nodes, {len(self.edges)} Edges.")

    # region DIJKSTRA ROUTING & BULKHEAD ISOLATION

    def dijkstra_evacuation_path(self, start_node_id, target_node_id=103): # 103 = Core Bunker
        """Computes optimal evacuation route using Dijkstra shortest-path algorithm."""
        dist = {nid: float('inf') for nid in self.nodes}
        prev = {nid: None for nid in self.nodes}
        dist[start_node_id] = 0.0
        pq = [(0.0, start_node_id)]

        while pq:
            d, curr = heapq.heappop(pq)
            if d > dist[curr]:
                continue
            if curr == target_node_id:
                break

            curr_node = self.nodes[curr]
            if not curr_node.is_operational:
                continue

            for neighbor_id, edge_id, edge_len in curr_node.edges:
                edge = self.edges[edge_id]
                # Sealed bulkheads or non-operational edges are impassable (infinite weight)
                if edge.is_sealed:
                    continue
                neighbor_node = self.nodes[neighbor_id]
                if not neighbor_node.is_operational:
                    continue

                new_d = d + edge_len
                if new_d < dist[neighbor_id]:
                    dist[neighbor_id] = new_d
                    prev[neighbor_id] = curr
                    heapq.heappush(pq, (new_d, neighbor_id))

        # Reconstruct path
        path = []
        curr = target_node_id
        while curr is not None:
            path.append(curr)
            curr = prev[curr]
        path.reverse()

        if path and path[0] == start_node_id:
            return path, dist[target_node_id]
        return [], float('inf')

    def trigger_disaster_hull_breach(self, compromised_node_id):
        """Simulates hull breach: seals adjacent bulkheads and isolates the node."""
        comp_node = self.nodes.get(compromised_node_id)
        if not comp_node:
            return False

        print(f"[!] HULL BREACH SENSOR TRIGGERED at Node {compromised_node_id} ({comp_node.name})!")
        comp_node.is_operational = False
        sealed_edges = []

        for neighbor_id, edge_id, _ in comp_node.edges:
            edge = self.edges[edge_id]
            edge.is_sealed = True
            sealed_edges.append(edge_id)

        print(f"[*] Sealed {len(sealed_edges)} Watertight Bulkheads: Edges {sealed_edges}")
        return True

    # endregion

# endregion

# region MAIN EXECUTION & DEMO
def main():
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
    os.makedirs(out_dir, exist_ok=True)

    builder = IstroriganGraphBuilder()
    builder.build_complete_network()

    # Test Evacuation Routing before and after breach
    start_test_node = 117 # Outer Evac shelter on Petal 2
    target_bunker = 103   # Core Sovereign Bunker

    path_normal, dist_normal = builder.dijkstra_evacuation_path(start_test_node, target_bunker)
    print(f"[*] Normal Evacuation Path from Node {start_test_node} to Bunker {target_bunker}:")
    print(f"    Path: {path_normal} (Distance: {dist_normal:.1f}m)")

    # Simulate Disaster: Hull breach at intermediate transit node
    breach_node = 114 # Intermediate station
    builder.trigger_disaster_hull_breach(breach_node)

    path_rerouted, dist_rerouted = builder.dijkstra_evacuation_path(start_test_node, target_bunker)
    print(f"[*] Re-routed Evacuation Path (Avoided Breached Node {breach_node}):")
    print(f"    Path: {path_rerouted} (Distance: {dist_rerouted:.1f}m)")

    # Export to JSON
    json_path = os.path.join(out_dir, "istrorigan_transit_graph.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "nodes": [n.to_dict() for n in builder.nodes.values()],
            "edges": [e.to_dict() for e in builder.edges.values()]
        }, f, indent=2)
    print(f"[+] Exported Transit Graph JSON: {json_path}")

    # Export to CSV (Nodes & Edges)
    csv_nodes_path = os.path.join(out_dir, "istrorigan_graph_nodes.csv")
    with open(csv_nodes_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["node_id", "name", "layer", "node_type", "petal_idx", "x", "y", "z", "capacity", "is_operational"])
        writer.writeheader()
        for n in builder.nodes.values():
            writer.writerow(n.to_dict())
    print(f"[+] Exported Graph Nodes CSV:   {csv_nodes_path}")

    csv_edges_path = os.path.join(out_dir, "istrorigan_graph_edges.csv")
    with open(csv_edges_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["edge_id", "start_node", "end_node", "edge_type", "distance_m", "max_throughput", "is_sealed"])
        writer.writeheader()
        for e in builder.edges.values():
            writer.writerow(e.to_dict())
    print(f"[+] Exported Graph Edges CSV:   {csv_edges_path}")


if __name__ == "__main__":
    main()
# endregion
