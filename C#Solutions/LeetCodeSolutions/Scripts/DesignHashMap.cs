namespace LeetCodeSolutions.Scripts;

public class MyHashMap
{
    private const int SIZE = 64;
    private List<(int key, int value)>[] buckets;

    public MyHashMap()
    {
        buckets = new List<(int key, int value)>[SIZE];
        for (int i = 0; i < SIZE; i++)
        {
            buckets[i] = new List<(int key, int value)>();
        }
    }

    private int Hash(int key)
    {
        return key % SIZE;
    }

    public void Put(int key, int value)
    {
        int index = Hash(key);
        var bucket = buckets[index];

        for (int i = 0; i < bucket.Count; i++)
        {
            if (bucket[i].key == key)
            {
                bucket[i] = (key, value);
                return;
            }
        }

        bucket.Add((key, value));
    }

    public int Get(int key)
    {
        int index = Hash(key);
        var bucket = buckets[index];

        foreach (var (k, v) in bucket)
        {
            if (k == key)
                return v;
        }

        return -1; // No encontrado
    }

    public void Remove(int key)
    {
        int index = Hash(key);
        var bucket = buckets[index];

        for (int i = 0; i < bucket.Count; i++)
        {
            if (bucket[i].key == key)
            {
                bucket.RemoveAt(i);
                return;
            }
        }
    }
}