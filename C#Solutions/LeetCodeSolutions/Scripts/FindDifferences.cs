namespace CSharpSolutions;
//https://leetcode.com/problems/find-the-difference/
public class FindDifferences
{
    public char FindTheDifference(string s, string t) {
        var sCharArray = s.ToCharArray().ToList();
        var tCharArray = t.ToCharArray().ToList();
        var shortestList = sCharArray.Count < tCharArray.Count ? sCharArray : tCharArray;
        sCharArray.Sort();
        tCharArray.Sort();

        for (int i = 0; i < shortestList.Count; i++)
        {
            if(sCharArray[i] != tCharArray[i])
                return tCharArray[i];
        }
        return tCharArray.Last();
    }
}