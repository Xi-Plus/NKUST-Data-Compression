function encode(s) {
    arr = s.split("").sort();
    low = 0;
    high = 1;
    for (c of s) {
        range = high - low;
        high = low + range * (arr.lastIndexOf(c) + 1) / arr.length;
        low = low + range * arr.indexOf(c) / arr.length;
    }
    return low;
}
encode("BILL GATES");
