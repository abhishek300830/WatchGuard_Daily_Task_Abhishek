import {
  Component,
  OnInit,
  Input,
  ViewEncapsulation,
  OnChanges,
  SimpleChanges,
  DoCheck,
  AfterContentInit,
  AfterContentChecked,
  AfterViewInit,
  AfterViewChecked,
  OnDestroy,
  ViewChild,
  ContentChild,
  ElementRef,
} from '@angular/core';

@Component({
  selector: 'app-server-element',
  templateUrl: './server-element.component.html',
  styleUrls: ['./server-element.component.css'],
})
export class ServerElementComponent
  implements
    OnInit,
    OnChanges,
    DoCheck,
    AfterContentInit,
    AfterContentChecked,
    AfterViewInit,
    AfterViewChecked,
    OnDestroy
{
  @Input('srvElement') element: { type: string; name: string; content: string };
  @Input('name') name: string;

  @ViewChild('heading', { static: true }) header: ElementRef;
  @ContentChild('contentParagraph', { static: true }) paragrah: ElementRef;

  constructor() {
    console.log('constructor Called');
  }

  ngOnInit(): void {
    console.log('Text Content : ', this.header.nativeElement.textContent);
    console.log(
      'Text Content of Paragrah : ',
      this.paragrah.nativeElement.textContent
    );
    console.log('ngOnInit called');
  }

  ngOnChanges(changes: SimpleChanges) {
    console.log('changes', changes);
    console.log('ngONChanges called');
  }

  ngDoCheck() {
    console.log('ngDoCheck Called');
  }

  ngAfterContentInit(): void {
    console.log(
      'Text Content of Paragrah : ',
      this.paragrah.nativeElement.textContent
    );
    console.log('ngAfterContentInit Called');
  }

  ngAfterContentChecked(): void {
    console.log('ngAfterContentChecked called');
  }

  ngAfterViewInit(): void {
    console.log('Text Content : ', this.header.nativeElement.textContent);

    console.log('ngAfterViewInit called');
  }

  ngAfterViewChecked(): void {
    console.log('ngAfterViewChecked');
  }

  ngOnDestroy(): void {
    console.log('ngOnDestroyCalled');
  }
}
