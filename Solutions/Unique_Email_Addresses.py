class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            temp = email.split("@")
            domain = temp[1]
            local_name = temp[0]

            reduced_local_name = ""
            for char in local_name:
                if char == "+":
                    break
                elif char == ".":
                    continue
                else:
                    reduced_local_name += char

            res.add(reduced_local_name + "@" + domain)

        return len(res)