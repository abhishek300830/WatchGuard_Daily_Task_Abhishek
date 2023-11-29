import { inject } from '@angular/core';
import {
  ActivatedRouteSnapshot,
  CanActivateFn,
  Router,
  RouterStateSnapshot,
} from '@angular/router';
import { AuthService } from './auth.service';
import { map, take } from 'rxjs/operators';

export const AuthGuard: CanActivateFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot
) => {
  const router = inject(Router);
  const authService = inject(AuthService);

  return authService.user.pipe(
    take(1),
    map((user) => {
      const isAuthenticated = !!user;
      if (!isAuthenticated) {
        return router.createUrlTree(['/auth']);
      } else {
        return true;
      }
    })
  );
};
