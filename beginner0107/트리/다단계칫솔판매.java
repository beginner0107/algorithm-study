import java.util.*;

class TreeNode {
    
    private String name;
    private int profit;
    private TreeNode parent;
    private ArrayList<TreeNode> children;
    
    TreeNode (String name) {
        this.name = name;
        this.profit = 0;
        this.parent = null;
        this.children = new ArrayList<>();
    }
    
    public String getName() {
        return name;
    }
    
    public int getProfit() {
        return profit;
    }
    
    public void setProfit(int profit) {
        this.profit = profit;
    }
    
    public TreeNode getParent() {
        return parent;
    }
    
    public void setParent(TreeNode parent) {
        this.parent = parent;
    }
    
    public ArrayList<TreeNode> getChildren() {
        return children;
    }
    
    public void addChildren(TreeNode child) {
        this.children.add(child);
    }
}

class 다단계칫솔판매 {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        Map<String, TreeNode> nodeMap = new HashMap<>();
        TreeNode root = new TreeNode("center");
        nodeMap.put("center", root);
        int n = enroll.length;
        for (int i = 0; i < n; i++) {
            
            TreeNode newNode = new TreeNode(enroll[i]);
            
            if (referral[i].equals("-")) {
                newNode.setParent(root);
            } else {
                TreeNode parent = nodeMap.get(referral[i]);
                newNode.setParent(parent);
                parent.addChildren(newNode);
            }
            nodeMap.put(enroll[i], newNode);
        }
        
        for (int i = 0; i < seller.length; i ++) {
            TreeNode node = nodeMap.get(seller[i]);
            int profit = amount[i] * 100;
            
            dist(node, profit);
        }
        
        int[] answer = new int[enroll.length];
        
        for (int i = 0; i < answer.length; i++) {
            answer[i] = nodeMap.get(enroll[i]).getProfit();
        }
        return answer;
    }
    
    void dist(TreeNode node, int profit) {
        int money = profit - (profit / 10);
        node.setProfit(node.getProfit() + money);
        
        if (node.getParent() != null && (profit / 10) >= 1) {
            dist(node.getParent(), profit / 10);
        }
    }
}