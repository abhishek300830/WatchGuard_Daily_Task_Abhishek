describe('first test', () => {
  let testVariable: any;

  beforeEach(() => {
    testVariable = {};
  });

  it('should be true if a is true', () => {
    testVariable.a = false;
    testVariable.a = true;
    expect(testVariable.a).toBe(true);
  });
});
