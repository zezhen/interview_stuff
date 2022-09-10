

// ConcurrentHashMap functions
// 1. get(key): return key mapped value or null
// 2. put(key, val): return the previous value associated with key, or null
// 3. putIfAbsent(key, val): return the previous value associated with the specified key, or null
// 4. replace(key, oldVal, newVal): Replaces the entry for a key only if currently mapped to a given value, return true if replaced
public class MultiSessionCart {

    public void addProduct(String sid, int pid, ConcurrentHashMap<String, Vector<Integer>> map) {
        Vector<Integer> vector = null;
        while (vector == null) {
            vector = map.putIfAbsent(sid, new Vector<Integer>());
        }

        vector.add(pid);

        while (map.replace(sid, vector, vector) == false) {
            vector = new Vector<Integer>(new Integer[]{pid});
            map.putIfAbsent(sid, vector);
        }
    }
}