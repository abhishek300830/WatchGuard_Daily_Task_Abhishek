import { TestBed } from '@angular/core/testing';
import { PostService } from './post.service';
import { HttpClient } from '@angular/common/http';
import { of } from 'rxjs';
import { Post } from 'src/app/components/posts/models/post';

describe('Post Service', () => {
  let httpClientSpy: jasmine.SpyObj<HttpClient>;
  let postService: PostService;
  let POSTS: Post[];

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
    httpClientSpy = jasmine.createSpyObj('HttpClient', ['get']);
    TestBed.configureTestingModule({
      providers: [
        PostService,
        {
          provide: HttpClient,
          useValue: httpClientSpy,
        },
      ],
    });
    postService = TestBed.inject(PostService);
  });

  describe('getPosts()', () => {
    it('should return expected post when get post is called', (done: DoneFn) => {
      httpClientSpy.get.and.returnValue(of(POSTS));
      postService.getPosts().subscribe({
        next: (posts) => {
          expect(posts).toEqual(POSTS);
          done();
        },
        error: () => {
          done.fail();
        },
      });
      expect(httpClientSpy.get).toHaveBeenCalledTimes(1);
    });
  });
});
