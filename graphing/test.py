from graphviz import Digraph
dot = Digraph()

dot.node("g", label="Graph")
# dot.node("g","Graph")

dot.edge("Session", "g")
dot.edge("g", "Placeholder")
dot.edge("g", "Variable")

print(dot.source)
# dot.render('./test.gv', view=True) #匯出pdf檔案
