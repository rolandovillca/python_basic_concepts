temp_module = __import__('vmware.ProducerSnippetBase', globals(), locals(), ["ProducerSnippetBase"], -1)
producer_snippet_base = getattr(temp_module, "ProducerSnippetBase")
setattr(producer_snippet_base, "print_text", lambda(self): "ZZZ")

r1 = file.print_msg()
x = file.ProducerSnippetBase()
x2 = file.ProducerSnippetBase()
r2 = x.print_text()
print r1
print r2
print x2.print_text()