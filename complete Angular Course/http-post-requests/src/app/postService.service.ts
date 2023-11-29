import { HttpClient, HttpEventType, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Post } from './post.model';
import { catchError, map, tap } from 'rxjs/operators';
import { Subject, throwError } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class PostService {
  error = new Subject<string>();

  constructor(private http: HttpClient) {}

  createAndStorePost(title: string, content: string) {
    const postData: Post = { title: title, content: content };

    this.http
      .post<{ name: string }>(
        'https://learning-angular-f5314-default-rtdb.firebaseio.com/posts.json',
        postData,{
          observe: 'response'
        }
      )
      .subscribe({
        next:(responseData) => {
          console.log(responseData);
        },
        error: error=>{
          this.error.next(error.message)
        }
      });
  }

  fetchPosts(){
    let searchParams = new HttpParams();
    searchParams = searchParams.append('print','pretty')
    searchParams = searchParams.append('custom','key')

    return this.http
      .get<{ [key: string]: Post }>(
        'https://learning-angular-f5314-default-rtdb.firebaseio.com/posts.json',
        {
          headers: new HttpHeaders({"custom-header":"hello"}),
          // params:new HttpParams().set('print','prity')
          params:searchParams
        }
      )
      .pipe(
        map((posts) => {
          const postsArray: Post[] = [];
          for (const key in posts) {
            if (posts.hasOwnProperty(key)) {
              postsArray.push({ ...posts[key], id: key });
            }
          }
          return postsArray;
        })
        ,
        catchError((error)=>{
          throw error
          // task like send analytics data
        })
      )
     
  }

  deletePosts(){
    return this.http.delete('https://learning-angular-f5314-default-rtdb.firebaseio.com/posts.json',{
      observe:'events'
    }).pipe(tap(
      (event)=>{
        console.log(event)
        if(event.type === HttpEventType.Sent){

        }
        if(event.type === HttpEventType.Response){ }
      }
    ))
  }
}
