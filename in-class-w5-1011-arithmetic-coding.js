function encode(s) {
    arr = s.split("").sort();
    table = {};
    for (c of s) {
        table[c] = [arr.indexOf(c) / arr.length, (arr.lastIndexOf(c) + 1) / arr.length];
    }
    low = 0;
    high = 1;
    for (c of s) {
        range = high - low;
        high = low + range * (arr.lastIndexOf(c) + 1) / arr.length;
        low = low + range * arr.indexOf(c) / arr.length;
    }
    return {
        "table": table,
        "value": low
    };
}

function decode(table, value) {
    res = "";
    while (value > 1e-7) {
        for (c in table) {
            if (value >= table[c][0] && value < table[c][1]) {
                res += c;
                value -= table[c][0];
                value /= (table[c][1] - table[c][0]);
                break;
            }
        }
    }
    return res;
}

res = encode("BILL GATES");
console.log("encode table:", res["table"]);
console.log("encode value:", res["value"]);

console.log("decode:", decode(res["table"], res["value"]));
