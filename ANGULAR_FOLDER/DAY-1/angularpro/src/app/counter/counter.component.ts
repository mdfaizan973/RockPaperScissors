import { Component } from '@angular/core';

@Component({
  selector: 'app-counter',
  templateUrl: './counter.component.html',
  styleUrls: ['./counter.component.css'],
})
export class CounterComponent {
  count: number = 0;

  increment(): void {
    this.count++;
  }

  decrement(): void {
    this.count--;
  }
}
