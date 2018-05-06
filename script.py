def run():
    try:
        result = gdb.execute("run")
    except:
        return None
    return result

def start():
    try:
        result = gdb.execute("start")
    except:
        return None
    return result

def c():
    try:
        result = gdb.execute("continue")
    except:
        return None
    return result
  
        
def br(addr):
    cmd = "b *{}".format(addr)
    
    try:
        result = gdb.execute(cmd, to_string=True)
    except:
        return None
    return result

def read_reg(reg):
    cmd = "p $" + reg
    
    try:
        result = gdb.execute(cmd, to_string=True)
    except:
        return None
    return int(result.split()[2], 16)


def read_mem(addr, _type):

    if not _type in {'b', 'h', 'w', 'g'}:
        print("Invalid argument")
        return None
    
    cmd = "x/{}x {}".format(n, addr)
    
    try:
        result = gdb.execute(cmd, to_string=True)
    except:
        return None
    
    return int(result.split()[1], 16)

def read_byte(addr):
    return read_mem(addr, 'b')

def read_word(addr):
    return read_mem(addr, 'h')

def read_dword(addr):
    return read_mem(addr, 'w')

def read_qword(addr):
    return read_mem(addr, 'g')

def read_string(addr):
    result = ''
    i = 0
    while True:
        c = read_byte(addr+i)
        if c == 0x00:
            break
        result += chr(c)
        i += 1
    return result
