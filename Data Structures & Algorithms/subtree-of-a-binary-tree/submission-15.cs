/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {    
    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null)
        {
            return true;
        }

        if (root == null)
        {
            return false;
        }

        if (CheckSubtree(root, subRoot))
        {
            return true;    
        }
        else
        {
            return (IsSubtree(root.left, subRoot) || IsSubtree(root.right, subRoot));
        }
    }

    public bool CheckSubtree(TreeNode node, TreeNode subNode)
    {
        if (node == null && subNode == null)
        {
            return true;
        }

        if (node != null && subNode != null && node.val == subNode.val)
        {
            return (CheckSubtree(node.left, subNode.left) 
                && CheckSubtree(node.right, subNode.right));
        }

        return false;
    }
}
