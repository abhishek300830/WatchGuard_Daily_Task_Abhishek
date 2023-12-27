import { PostService } from 'src/app/services/Post/post.service';
import { Post } from './models/post';
import { PostsComponent } from './posts.component';
import { of } from 'rxjs';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, Input, OnInit } from '@angular/core';
import { By } from '@angular/platform-browser';
import { PostComponent } from '../post/post.component';
import { RouterTestingModule } from '@angular/router/testing';

// @Component({
//   selector: 'app-post',
//   template: '<div></div>',
// })
// class FakePostComponent {
//   @Input() post!: Post;
// }

describe('Posts Component', () => {
  let POSTS: Post[];
  let component: PostsComponent;
  let mockPostService: any;
  let fixture: ComponentFixture<PostsComponent>;

  beforeEach(() => {
    POSTS = [
      {
        id: 1,
        body: 'body 1',
        title: 'title 1',
      },
      {
        id: 2,
        body: 'body 2',
        title: 'title 2',
      },
      {
        id: 3,
        body: 'body 3',
        title: 'title 3',
      },
    ];
    mockPostService = jasmine.createSpyObj(['getPosts', 'deletePost']);
    // component = new PostsComponent(mockPostService);
    TestBed.configureTestingModule({
      imports: [RouterTestingModule],
      declarations: [PostsComponent, PostComponent],
      providers: [
        // PostsComponent,
        { provide: PostService, useValue: mockPostService },
      ],
    });
    // component = TestBed.inject(PostsComponent);
    fixture = TestBed.createComponent(PostsComponent);
    component = fixture.componentInstance;
  });

  it('should create exact same number of PostComponent with posts', () => {
    mockPostService.getPosts.and.returnValue(of(POSTS));
    fixture.detectChanges();
    const postComponentDEs = fixture.debugElement.queryAll(
      By.directive(PostComponent)
    );
    expect(postComponentDEs.length).toBe(POSTS.length);
  });

  it('should check whether exact post is sending to post component', () => {
    mockPostService.getPosts.and.returnValue(of(POSTS));
    fixture.detectChanges();
    const postComponentDEs = fixture.debugElement.queryAll(
      By.directive(PostComponent)
    );
    for (let index = 0; index < POSTS.length; index++) {
      const postComponentInstanse = postComponentDEs[index].componentInstance;
      expect(postComponentInstanse.post.title).toEqual(POSTS[index].title);
    }
  });

  it('should set posts from service directly', () => {
    mockPostService.getPosts.and.returnValue(of(POSTS));
    fixture.detectChanges();
    expect(component.posts.length).toBe(3);
  });

  it('should create one child component for each post', () => {
    mockPostService.getPosts.and.returnValue(of(POSTS));
    fixture.detectChanges();
    const debugElement = fixture.debugElement;
    const postElement = debugElement.queryAll(By.css('.posts'));
    expect(postElement.length).toBe(POSTS.length);
  });

  describe('Delete', () => {
    beforeEach(() => {
      mockPostService.deletePost.and.returnValue(of(true));
      component.posts = POSTS;
    });

    it('should delete the selected post from the posts', () => {
      component.delete(POSTS[1]);
      expect(component.posts.length).toBe(2);
    });

    it('should delete the actual selected post ', () => {
      component.delete(POSTS[1]);

      for (let post of component.posts) {
        expect(post).not.toEqual(POSTS[1]);
      }
    });

    it('should call delete method only once', () => {
      component.delete(POSTS[1]);
      expect(mockPostService.deletePost).toHaveBeenCalledTimes(1);
    });
  });
});
