import { Component, OnDestroy, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subscription, map } from 'rxjs';
import { Post } from './post.model';
import { PostService } from './postService.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit,OnDestroy {
  displayText = 'hello this is a string';
  loadedPosts: Post[] = [];
  isFetching = false;
  error = null;
  private errorSub:Subscription


  constructor(private http: HttpClient, private postService: PostService) {}

  ngOnInit() {
    this.errorSub = this.postService.error.subscribe((errorMessage)=>{
      this.error = errorMessage
    })
    this.onFetchPosts()
  }

  onCreatePost(postData: Post) {
    // Send Http request
    this.postService.createAndStorePost(postData.title, postData.content);
  }

  onFetchPosts() {
    // Send Http request
    this.isFetching = true;
    this.postService.fetchPosts().subscribe({
      next:(posts) => {
        this.isFetching = false;
        this.loadedPosts = posts;
      },
      error: (error)=>{
        this.isFetching = false
        this.error = error.message
      }
    });
  }

  onClearPosts() {
    // Send Http request
    this.postService.deletePosts().subscribe(() => {
      this.loadedPosts = [];
    });
  }

  onHandleError(){
    this.error = null
  }

  ngOnDestroy(): void {
      this.errorSub.unsubscribe()
  }
}
