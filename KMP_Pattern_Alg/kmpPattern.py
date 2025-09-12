"""
This code computes the LPS (Longest Prefix which is also Suffix) array for the given pattern,
which is used in the Knuth-Morris-Pratt (KMP) string matching algorithm.

It efficiently helps the KMP algorithm skip unnecessary comparisons by knowing how much of the
 pattern has already been matched when a mismatch occurs.

Would you like to see this LPS array used in a full KMP search against the text string?

"""


def compute_lps(pattern_in, lps_in, debug_in=False):
    length = 0  # Length of the current longest prefix-suffix
    index = 1  # We start comparing from the second character

    # Iterate through the pattern to build the LPS array
    while index < len(pattern_in):
        if debug_in:
            print(index, pattern_in[index], length, pattern_in[length])  # Debug info

        # Case 1: Current characters match
        if pattern_in[index] == pattern_in[length]:
            if debug_in:
                print("\t", pattern_in[index], "=", pattern_in[length])  # Debug print
            length += 1  # Increase length of current matching prefix-suffix
            lps_in[index] = length  # Set LPS value at current index
            index += 1  # Move to the next character

        else:
            # Case 2: Characters don't match

            # If length is not 0, fall back to previous LPS
            if length != 0:
                if debug_in:
                    print("\tlength != 0\t", length, lps_in[length - 1])  # Debug print
                length = lps_in[length - 1]  # Try shorter prefix-suffix
                # Note: index not incremented here, we re-check same index with updated length

            else:
                # If length is 0, we can't fall back — so LPS at this index is 0
                if debug_in:
                    print("\tlength == 0\t")  # Debug print
                lps_in[index] = 0
                index += 1  # Move to the next character


pattern = 'AAACAAAAAC'  # Pattern we're computing the LPS for
longest_proper_suffix = [0] * len(pattern)  # Initialize LPS array with all 0s

text = 'ABABDABACDABABCABAB'  # Unused here, possibly for later KMP matching

compute_lps(pattern_in=pattern, lps_in=longest_proper_suffix, debug_in=True)
print(longest_proper_suffix)  # Final LPS array
