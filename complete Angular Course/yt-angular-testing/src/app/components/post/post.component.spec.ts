import { first } from 'rxjs';
import { Post } from '../posts/models/post';
import { PostComponent } from './post.component';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';

describe('Post Component', () => {
  let fixture: ComponentFixture<PostComponent>;
  let component: PostComponent;
  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PostComponent],
      // schemas: [NO_ERRORS_SCHEMA],
      imports: [RouterTestingModule],
    });

    fixture = TestBed.createComponent(PostComponent);
    component = fixture.componentInstance;
  });

  it('should create component using testBed', () => {
    expect(component).toBeDefined();
  });

  it('should render the post title in the anchor tag', () => {
    const post: Post = { id: 1, body: 'body 1', title: 'title 1' };
    component.post = post;
    fixture.detectChanges();
    const postElement: HTMLElement = fixture.nativeElement;
    const a = postElement.querySelector('a');
    expect(a?.textContent).toContain(post.title);
  });

  it('should render the post title in the anchor tag using debug element', () => {
    const post: Post = { id: 1, body: 'body 1', title: 'title 1' };
    component.post = post;
    fixture.detectChanges();
    const postDebugElement: DebugElement = fixture.debugElement;
    const aElement = postDebugElement.query(By.css('a')).nativeElement;
    expect(aElement?.textContent).toContain(post.title);
  });

  it('should raise an event when delete post is clicked', () => {
    const comp = new PostComponent();
    const post: Post = { id: 1, body: 'body 1', title: 'title 1' };
    comp.post = post;

    comp.delete.pipe(first()).subscribe((selectedPost) => {
      expect(selectedPost).toBe(post);
    });

    comp.onDeletePost(new MouseEvent('click'));
  });
});
