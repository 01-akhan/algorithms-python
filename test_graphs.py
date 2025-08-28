from src.graphs import bfs, dfs, dijkstra

def test_bfs_dfs():
    adj = {0:[1,2],1:[2],2:[0,3],3:[]}
    assert bfs(adj, 0)[0] == 0
    assert set(dfs(adj, 0)) == {0,1,2,3}

def test_dijkstra():
    wadj = {0:[(1,4),(2,1)], 1:[(3,1)], 2:[(1,2)], 3:[]}
    dist = dijkstra(wadj, 0)
    # expected shortest 0->2->1->3: 1 + 2 + 1 = 4
    assert dist[3] == 4