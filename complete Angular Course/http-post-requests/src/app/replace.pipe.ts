import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'replace'
})
export class ReplacePipe implements PipeTransform {

  transform(value: string, oldString:string,newString:string) {
    if ( value.includes(oldString)){
      const newValue = value.replace(oldString,newString)
      return newValue
    }else{
      return value
    }
  }

}
