class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()
        result = []
        
        for folder in folders:
            if not result or not folder.startswith(result[-1] + "/"):
                result.append(folder)

        return result