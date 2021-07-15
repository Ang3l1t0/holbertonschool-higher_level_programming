#!/usr/bin/node
exports.converter = function (base) {
  return (conversion) => {
    return conversion.toString(base);
  };
};
