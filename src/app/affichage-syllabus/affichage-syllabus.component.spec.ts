import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AffichageSyllabusComponent } from './affichage-syllabus.component';

describe('AffichageSyllabusComponent', () => {
  let component: AffichageSyllabusComponent;
  let fixture: ComponentFixture<AffichageSyllabusComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AffichageSyllabusComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AffichageSyllabusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
