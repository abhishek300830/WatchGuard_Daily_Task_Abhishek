import { Directive, ElementRef, OnInit } from '@angular/core';
import { LoggingService } from 'src/app/logging.service';

@Directive({
  selector: '[appBasicHighlight]',
  providers: [LoggingService],
})
export class BasicHighlightDirective implements OnInit {
  constructor(
    private elementRef: ElementRef,
    private loggingService: LoggingService
  ) {}

  ngOnInit(): void {
    this.elementRef.nativeElement.style.backgroundColor = 'green';
    this.loggingService.loggingStatus('color Changed');
  }
}
