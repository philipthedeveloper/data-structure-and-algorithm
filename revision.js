console.clear();
const isValid = (s) => {
  if (s.length % 2 !== 0) return false;
  let bracketPairMap = {
    "}": "{",
    "{": "}",
    ")": "(",
    "(": ")",
    "]": "[",
    "[": "]",
  };
  const sType = s[0] === bracketPairMap[s[1]] ? "pair" : "nested";
  if (sType === "pair") {
    for (let i = 0; i < s.length; i += 2) {
      if (s[i] !== bracketPairMap[s[i + 1]]) {
        return false;
      }
    }
  } else {
    let lastIndex = s.length - 1;
    let midpoint = s.length / 2;
    for (let i = 0; i < midpoint; i++) {
      if (s[i] !== bracketPairMap[s[lastIndex - i]]) {
        return false;
      }
    }
  }
  return true;
};
console.log(isValid("(){}[]"));
console.log(isValid("({]}"));
console.log(isValid("{()}"));
