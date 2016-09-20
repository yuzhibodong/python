document.writeln('Hello, world!');

var flight = {
    airline: "Oceanic",
    number: 815,
    departure: {
        IATA: "SYD",
        time: "2004-09-22 14:55",
        city: "Sydney"
    },
    arrival: {
        IATA: "LAX",
        time: "2004-09-23 10:42",
        city: "Los Angeles"
    }
};

flight.departure.IATA;

var stooge = {
    "first_name": "Jerome",
    "last_name": "Howard",
};

if (typeof Object.beget !== 'function') {
    Object.create = function(o) {
        var F = function() {};
        F.prototype = o;
        return new F();
    };
}

var another_stooge = Object.create(stooge);

var name;
for (name in another_stooge) {
    if (typeof another_stooge[name] !== 'function') {
        document.writeln(name + ': ' + another_stooge[name]);
    }
}

var add = function(a, b) {
    return a + b;
};

var myObject = {
    value: 0,
};

myObject.double = function() {
    var that = this; // 解决方法

    var helper = function() {
        // 此处的this被绑定到全局对象, 是错误
        // this === window
        that.value = add(that.value, that.value);
    };

    helper(); // 以函数的形式调用 helper
};

// 以方法的形式调用double

myObject.double();
document.writeln(myObject.value);

var sum = function() {
    var sum = 0;
    for (var i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
};

document.writeln(sum(4, 8, 15, 16, 23, 42));    //108

var myObject = (function () {
    var value = 0;

    return {
        increment: function (inc) {
            value += typeof inc === 'number' ? inc : 1;
        },
        getValue: function () {
            return value;
        }
    };
}());
