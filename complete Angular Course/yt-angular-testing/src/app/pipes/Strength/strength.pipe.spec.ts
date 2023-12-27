import { Pipe } from '@angular/core';
import { StrengthPipe } from './strength.pipe';

describe('StrengthPipe', () => {
  let pipe: any;

  beforeEach(() => {
    pipe = new StrengthPipe();
  });

  it('create an instance', () => {
    expect(pipe).toBeTruthy();
  });

  it('should display weak if 5 value', () => {
    expect(pipe.transform(5)).toEqual('5(Weak)');
  });
  it('should display strong if 10 value', () => {
    expect(pipe.transform(10)).toEqual('10(Strong)');
  });
  it('should display strongest if 30 value', () => {
    expect(pipe.transform(30)).toEqual('30(Strongest)');
  });
});
