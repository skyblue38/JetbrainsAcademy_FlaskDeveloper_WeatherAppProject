markdown_symbols = ["*", "_", "~", "`"]
cleaned_line_list = []
for w in input().split():
    for c in markdown_symbols:
        if len(w) == 1:
            continue
        while w.startswith(c):
            w = w[1:]
        while w.endswith(c):
            w = w[:-1]
    if len(w) > 0:
        cleaned_line_list.append(w)
print(" ".join(cleaned_line_list))
