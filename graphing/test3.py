from graphviz import Source
temp = """
digraph {
  node [shape=circle,fontsize=8,fixedsize=true,width=0.9]; 
  edge [fontsize=8]; 
  

  "Back" [shape="egg" color="green" style="filled" fillcolor="yellow"];
  "Forth" [shape="house" color="red"];
  "Other" [shape="invtriangle" color="blue"];

  "Back" -> "Forth" [color="orange" label="weee"];
  "Forth" -> "Back" [color="purple" label="eeew"];

  "Other" -> "Forth"
  "Other" -> "Back"
}
"""
Source(temp).view()
