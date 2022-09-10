# Concurrency problem
----

Function for chm 

1.  val get (key)
2.  pre\_val put(key, val)
3.  pre\_val putIfAbsent(key, val)
4.  boolean replace(key, cur\_val, new\_val)

public class MultiSessionCart {

 void addProduct( string sid, int pid, concurrentHashMap map) {

 }
}

Considering hmp is not controlled by this class, other class might add data or remove keys from hmp, what should do in add product function to guarantee it’s thread safe.






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
            vector = new Vector<Integer>(new Integer\[\]{pid});
            map.putIfAbsent(sid, vector);
        }
    }
}

----

- Date: 2019-03-12
- Tags: #Interview/Programing 



