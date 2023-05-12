class CODE_GENERATOR:
    def __init__(self, beautifier=True):
        self.var_num = 0
        self.intc = []
        self.bytec = []

        self.code = []
        self.pc = 0
        self.stack = []

        self.itxn_num = 0
        self.beautifier = beautifier

    def get_new_var(self):
        self.var_num += 1
        return "var_%d" % (self.var_num - 1)

    def add_code(self, code):
        self.code.append(code)

    def stack_pop(self):
        if self.beautifier:
            return self.stack.pop()
        else:
            varname = self.get_new_var()
            self.add_code("%s = stackpop()\n" % varname)
            return varname

    def stack_push(self, d):
        if self.beautifier:
            self.stack.append(d)
        else:
            self.add_code("stackpush(%s)\n" % d)
    

    def new_itxn(self):
        self.itxn_num += 1
        self.add_code("\n//NEW Inner Txn [%d]" % self.itxn_num)

    def record_itxn(self):
        self.prev_itxn_num = self.itxn_num

    def get_recorded_itxn(self):
        return self.prev_itxn_num
    
    def get_now_itxn(self):
        return self.itxn_num

    def set_version(self, line):
        self.code.append(line)

    def get_result(self):
        return "\n".join(self.code)

    def get_ctx_full_name(self, varname):
        return "CTX.%s" % varname

    def add_ctx_var(self, varname, code):
        self.add_code("%s = %s" % (self.get_ctx_full_name(varname), code))

    def set_branch(self, label):
        if ":" not in label:
            label += ":"
        self.add_code("%s" % label)
    
