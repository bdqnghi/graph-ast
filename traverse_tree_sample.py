import pickle
import sys

file_path = "sample_files/Java/Bubblesort.pkl"

def load_pickle(path):
    """Builds an AST from a script."""
   
    with open(path, 'rb') as file_handler:
        tree = pickle.load(file_handler)
      
        return tree
    return None
#   return ast.parse(script)


def traverse_tree(root):
    num_nodes = 1
    queue = [root]

    root_json = {
        "node": str(root.kind),

        "children": []
    }
    queue_json = [root_json]
    while queue:
      
        current_node = queue.pop(0)
        num_nodes += 1
        # print (_name(current_node))
        current_node_json = queue_json.pop(0)


        children = [x for x in current_node.child]
        queue.extend(children)
       
        for child in children:
            print(child)
            # print "##################"
            #print child.kind

            child_json = {
                "node": str(child.kind),
                "children": []
            }

            current_node_json['children'].append(child_json)
            queue_json.append(child_json)
            # print current_node_json
  
    return root_json, num_nodes

data = load_pickle(file_path)
print(data)
# root = data.element
# traverse_tree(root)