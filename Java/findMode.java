class Solution {
    public int[] findMode(TreeNode root) {
        // create a int int key value pair hash map, for Map.entry denote entry we will access each entry of int int pairs of c, if it is == to max occuring number = Collections.max (returns max value in hashmap), add this to an int[] array to match return type
        HashMap<Integer, Integer> c = new HashMap<>();
        List<Integer> maxKeys = new ArrayList<>();

        inorder(root, c);

        int maxValue = Collections.max(c.values());

        for (Map.Entry<Integer, Integer> entry : c.entrySet()){
            if (entry.getValue() == maxValue){
                maxKeys.add(entry.getKey());
            }
        }

        int[] res = new int[maxKeys.size()];
        for (int i = 0; i < maxKeys.size(); i++){
            res[i] = maxKeys.get(i);
        }

        return res;
        
    }
    // private helper method recursively traverses in order the tree and adds it to count (c). .merge will add node.val as the key, then the value pair will be one if nodeval is null in c, or sum if it exists.  
    private void inorder(TreeNode node, HashMap<Integer, Integer> c){
        if (node == null) return;

        inorder(node.left, c);
        c.merge(node.val, 1, Integer::sum);
        inorder(node.right, c);
    }
}