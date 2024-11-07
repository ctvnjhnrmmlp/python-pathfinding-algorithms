# Python Pathfinding Algorithms

## Overview

**Greedy Best-First Search**

A search algorithm that expands nodes based solely on their heuristic value, which estimates the distance from the current node to the goal

We use the Manhattan distance as our heuristic, calculating the distance from a node to the treasure (goal) by summing the absolute differences between their x and y coordinates.

**A Star Search**

A pathfinding algorithm that considers both the actual cost to reach a node from the start (g(n)) and the estimated cost to reach the goal from that node (h(n))

In this implementation, g(n) is the accumulated cost from the start to the current node, while h(n) is the Manhattan distance to the goal

## Run

python main.py

## Description

## Screenshots

## Paths

## Time Taken

## Path Lengths
