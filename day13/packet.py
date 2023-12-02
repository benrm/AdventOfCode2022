def ParsePacket(line, i=0, outer=True):
    if line[i] != "[":
        raise Exception("Unexpected character at %d: %s" % (i, line[i]))
    packet = []
    i += 1
    while i < len(line):
        if line[i] == "[":
            ret = ParsePacket(line, i, False)
            packet.append(ret[0])
            i = ret[1]
        else:
            number = ""
            while line[i] != "," and line[i] != "]":
                number += line[i]
                i += 1
            if len(number) > 0:
                packet.append(int(number))
            if line[i] == "]":
                if outer:
                    return packet
                else:
                    return (packet, i+1)
            elif line[i] == ",":
                i += 1
            else:
                raise Exception("Unexpected character at %d: %s" % (i, line[i]))

def ComparePackets(left, right):
    for i in range(len(left)):
        if i >= len(right):
            break
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return 1
            elif left[i] > right[i]:
                return -1
            else:
                continue
        elif isinstance(left[i], list) and isinstance(right[i], list):
            ret = ComparePackets(left[i], right[i])
            if ret != 0:
                return ret
            else:
                continue
        elif isinstance(left[i], int) and isinstance(right[i], list):
            ret = ComparePackets([left[i]], right[i])
            if ret != 0:
                return ret
            else:
                continue
        elif isinstance(left[i], list) and isinstance(right[i], int):
            ret = ComparePackets(left[i], [right[i]])
            if ret != 0:
                return ret
            else:
                continue
        else:
            raise Exception("Packet contains non-list non-int")
    if len(right) < len(left):
        return -1
    elif len(right) > len(left):
        return 1
    else:
        return 0
