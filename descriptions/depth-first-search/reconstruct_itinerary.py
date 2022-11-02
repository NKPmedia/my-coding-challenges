""" 
Reconstruct Itinerary

Reference: https://leetcode.com/problems/reconstruct-itinerary/

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
["JFK", "LGB"]. 

Note: smaller lexican order meaning that when sorting the string, you would give ["JFK", "LGA"], which is the smaller lexical order.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example: 
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Solution: First we need to create an adjacency list. Then we can use DFS to
find the path. Note that we may go along an edge and find out that it is not a
valid path and will have to backtrack and try the other edge.

Time Complexity: O(E) -> E is the number of edges. At worst case, we will have
to backtrack through some edges and therefore could be O(E^2).

Memory Complexity: O(E) -> E is the number of edges. Recursive call stack and
hashmap. 
"""