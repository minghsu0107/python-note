from graphviz import Source
temp = """
digraph {
  "A" [shape="circle"];
  "B" [shape="rectangle"];
  "C" [shape="diamond"];

  "A" -> "B" [label="A to B"];
  "B" -> "C" [label="B to C"];
  "A" -> "C" [label="A to C"];
}
"""
#s = Source(temp, filename="test2.gv", format="pdf")
s = Source(temp)
s.view()