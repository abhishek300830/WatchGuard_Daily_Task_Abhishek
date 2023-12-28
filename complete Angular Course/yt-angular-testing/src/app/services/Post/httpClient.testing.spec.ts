import { HttpClient } from '@angular/common/http';
import { TestBed } from '@angular/core/testing';

import {
  HttpClientTestingModule,
  HttpTestingController,
} from '@angular/common/http/testing';

let testUrl = '/data';

interface Data {
  name: string;
}

describe('HTTP Client Testing Module Demonstration', () => {
  let httpClient: HttpClient;
  let httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
    });

    httpClient = TestBed.inject(HttpClient);
    httpTestingController = TestBed.inject(HttpTestingController);
  });

  it('should call the test url with get request', () => {
    httpClient.get<Data>(testUrl).subscribe();
    const req = httpTestingController.expectOne(testUrl);
    req.flush({ name: 'Test Data' });
    expect(req.request.method).toBe('GET');
  });

  it('should test multiple requests', () => {
    const testData: Data[] = [{ name: 'Leela' }, { name: 'Leela Web Dev' }];

    httpClient.get<Data[]>(testUrl).subscribe((data) => {
      expect(data.length).toEqual(0);
    });

    httpClient.get<Data[]>(testUrl).subscribe((data) => {
      expect(data).toEqual([testData[0]]);
    });

    httpClient.get<Data[]>(testUrl).subscribe((data) => {
      expect(data).toEqual(testData);
    });

    const requests = httpTestingController.match(testUrl);
    expect(requests.length).toEqual(3);

    requests[0].flush([]);
    requests[1].flush([testData[0]]);
    requests[2].flush(testData);
  });
});
