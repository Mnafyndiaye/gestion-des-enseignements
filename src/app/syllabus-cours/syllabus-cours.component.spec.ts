import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SyllabusCoursComponent } from './syllabus-cours.component';

describe('SyllabusCoursComponent', () => {
  let component: SyllabusCoursComponent;
  let fixture: ComponentFixture<SyllabusCoursComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SyllabusCoursComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SyllabusCoursComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
