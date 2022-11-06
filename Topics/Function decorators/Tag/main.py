def tagged(from_input):
    def title_wrapper(inp):
        inp = "<title>" + inp.strip() + "</title>"
        return from_input(inp)

    return title_wrapper
