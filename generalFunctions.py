def smartInput(msg:str,datatype:type,bounds=None):
    while True:
        try:
            user = datatype(input(msg))
            if bounds != None:
                if bounds[0] <= user <= bounds[1]:
                    continue
                else:
                    raise("ValueError")
            break
        except ValueError:
            continue

    return user