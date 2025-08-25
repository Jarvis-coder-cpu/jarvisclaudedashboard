export function getPromptReflection(input) {
  return input.length > 100 ? input.slice(0, 100) + '…' : input;
}
