import { Injectable, Output } from '@angular/core';
import { UserDetailModel } from './app.model';
import { Subject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class UserService {
  public userDetails: UserDetailModel = new UserDetailModel();

  newSubject = new Subject<Boolean>();
}
