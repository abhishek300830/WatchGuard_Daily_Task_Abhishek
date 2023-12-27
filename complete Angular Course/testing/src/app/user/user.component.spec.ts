import { TestBed, fakeAsync, tick, waitForAsync } from '@angular/core/testing';

import { UserComponent } from './user.component';
import { UserService } from './user.service';
import { DataService } from '../shared/data.service';

// describe('UserComponent', () => {
//   let component: UserComponent;
//   let fixture: ComponentFixture<UserComponent>;

//   beforeEach(async () => {
//     await TestBed.configureTestingModule({
//       declarations: [ UserComponent ]
//     })
//     .compileComponents();

//     fixture = TestBed.createComponent(UserComponent);
//     component = fixture.componentInstance;
//     fixture.detectChanges();
//   });

//   it('should create', () => {
//     expect(component).toBeTruthy();
//   });
// });

describe('UserComponent', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UserComponent],
    });
  });

  it('should create a app', () => {
    let fixture = TestBed.createComponent(UserComponent);
    let app = fixture.debugElement.nativeElement;
    expect(app).toBeTruthy();
  });

  it('should use user name from service', () => {
    let fixture = TestBed.createComponent(UserComponent);
    let app = fixture.debugElement.componentInstance;
    let userService = fixture.debugElement.injector.get(UserService);
    fixture.detectChanges();
    expect(userService.user.name).toEqual(app.user.name);
  });

  it('should display username if user is logged in', () => {
    let fixture = TestBed.createComponent(UserComponent);
    let app = fixture.debugElement.componentInstance;
    app.isLoggedIn = true;
    fixture.detectChanges();
    let compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('p').textContent).toContain(app.user.name);
  });

  it('should not fetch data successfully if not called async', () => {
    let fixture = TestBed.createComponent(UserComponent);
    let app = fixture.debugElement.componentInstance;
    let dataService = fixture.debugElement.injector.get(DataService);
    let spy = spyOn(dataService, 'getDetails').and.returnValue(
      Promise.resolve('Data')
    );
    fixture.detectChanges();
    expect(app.data).toBe(undefined);
  });

  // it('should fetch data successfully if called async', fakeAsync(() => {
  //   let fixture = TestBed.createComponent(UserComponent);
  //   let app = fixture.debugElement.componentInstance;
  //   let dataService = fixture.debugElement.injector.get(DataService);
  //   let spy = spyOn(dataService, 'getDetails').and.returnValue(
  //     Promise.resolve('Data')
  //   );
  //   fixture.detectChanges();
  //   tick();
  //   expect(app.data).toBe('Data');

  //   // fixture.whenStable().then(() => {
  //   //   expect(app.data).toBe('Data');
  //   // });
  // }));
});
