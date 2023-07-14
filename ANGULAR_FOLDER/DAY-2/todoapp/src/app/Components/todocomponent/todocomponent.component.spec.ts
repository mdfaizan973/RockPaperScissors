import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TodocomponentComponent } from './todocomponent.component';

describe('TodocomponentComponent', () => {
  let component: TodocomponentComponent;
  let fixture: ComponentFixture<TodocomponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TodocomponentComponent]
    });
    fixture = TestBed.createComponent(TodocomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
