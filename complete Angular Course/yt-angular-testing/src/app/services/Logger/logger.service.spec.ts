import { TestBed } from '@angular/core/testing';
import { LoggerService } from './logger.service';

describe('LoggerService', () => {
  let service: LoggerService;
  beforeEach(() => {
    // service = new LoggerService();

    TestBed.configureTestingModule({
      providers: [LoggerService],
    });
    service = TestBed.inject(LoggerService);
  });

  it('it should not have any message at starting', () => {
    expect(service.messages.length).toBe(0);
  });

  it('should add messages when log method is called ', () => {
    service.log('msg');
    expect(service.messages.length).toBe(1);
  });

  it('should clear all messges when clear is called', () => {
    service.log('message');
    service.clear();
    expect(service.messages.length).toBe(0);
  });
});

// import { TestBed } from '@angular/core/testing';

// import { LoggerService } from './logger.service';

// describe('LoggerService', () => {
//   let service: LoggerService;

//   beforeEach(() => {
//     TestBed.configureTestingModule({});
//     service = TestBed.inject(LoggerService);
//   });

//   it('should be created', () => {
//     expect(service).toBeTruthy();
//   });
// });
