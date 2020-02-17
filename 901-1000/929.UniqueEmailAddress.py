#
# 929. Unique Email Addresses
#
# Every email consists of a local name and a domain name, separated by the @
# sign.
#
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com
# is the domain name.
#
# Besides lowercase letters, these emails may contain '.'s or '+'s.
#
# If you add periods ('.') between some characters in the local name part of an
# email address, mail sent there will be forwarded to the same address without
# dots in the local name.  For example, "alice.z@leetcode.com" and
# "alicez@leetcode.com" forward to the same email address.  (Note that this
# rule does not apply for domain names.)
#
# If you add a plus ('+') in the local name, everything after the first plus
# sign will be ignored. This allows certain emails to be filtered, for example
# m.y+name@email.com will be forwarded to my@email.com. (Again, this rule does
# not apply for domain names.)
#
# It is possible to use both of these rules at the same time.
#
# Given a list of emails, we send one email to each address in the list.  How
# many different addresses actually receive mails?
#

int numUniqueEmails(char **emails, int emailsSize) {
    char unique[100][100] = {0};
    char email[100] = {0};
    int uniquesize = 0;
    int found;
    int k, j;
    for (int i = 0; i < emailsSize; i++) {
        found = 0;
        k = j = 0;
        while (emails[i][j] != '@') {
            if (emails[i][j] == '+')
                found = 1;
            else if (!found && emails[i][j] != '.')
                email[k++] = emails[i][j];
            j++;
        }
        while (emails[i][j]) {
            email[k++] = emails[i][j++];
        }
        email[k] = 0;
        found = 0;
        for (k = 0; k < uniquesize && !found; k++)
            if (strcmp(email, unique[k]) == 0)
                found = 1;
        if (!found) {
            strcpy(unique[uniquesize++], email);
        }
    }
    return uniquesize;
}