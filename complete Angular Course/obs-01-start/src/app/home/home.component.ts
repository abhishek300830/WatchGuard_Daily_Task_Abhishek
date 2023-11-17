import { Component, OnDestroy, OnInit } from '@angular/core';
import { Observable, Subscription, interval } from 'rxjs';
import { filter, map } from 'rxjs/operators';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit, OnDestroy {
  private obsSubscription: Subscription;
  constructor() {}

  ngOnInit() {
    // this.obsSubscription = interval(1000).subscribe((count) => {
    //   console.log('count', count);
    // });
    //  pure custom observable
    const customIntervalObservable = new Observable((subscriber) => {
      subscriber.next(1);
      subscriber.next(2);

      subscriber.next(3);
      // setTimeout(() => {
      //   subscriber.error('error occured');
      // }, 2000);

      // uncomment this for error part
      let count = 4;
      // if (count > 3) {
      //   subscriber.error(new Error('my custom Error'));
      // }

      setTimeout(() => {
        subscriber.next(4);
        subscriber.complete();
      }, 2000);
    });

    const pipedCustomIntervalObsevable = customIntervalObservable.pipe(
      filter((data: number) => {
        return data % 2 == 0;
      }),
      map((data) => {
        return 'piped data : ' + data;
      })
    );

    this.obsSubscription = pipedCustomIntervalObsevable.subscribe(
      (data) => {
        console.log('data', data);
      },
      (error) => {
        alert('counter is greater than 3');
        console.error('error: ', error);
      },
      () => {
        console.log('observable Completed');
      }
    );
  }
  ngOnDestroy(): void {
    this.obsSubscription.unsubscribe();
    console.log('unsubscribing');
  }
}
