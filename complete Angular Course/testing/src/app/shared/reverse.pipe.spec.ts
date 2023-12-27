import { ReversePipe } from './reverse.pipe';

describe('Reverse Pipe', () => {
  it('should create a pipe', () => {
    let reversePipe = new ReversePipe();
    expect(reversePipe.transform('hello')).toEqual('olleh');
  });
});
