import 'dart:convert';
import 'dart:io';

import 'package:csca_prep/content/models.dart';
import 'package:flutter_test/flutter_test.dart';

/// Checks the built assets: every paper resolves to real questions in the right pool.
void main() {
  final forms = jsonDecode(File('assets/data/forms.json').readAsStringSync()) as List<Object?>;
  final papers = [for (final form in forms) Paper.fromJson(form! as Json)];
  final questions = <String, Question>{};
  for (final file in Directory('assets/data').listSync().whereType<File>()) {
    final name = file.uri.pathSegments.last;
    if (!name.startsWith('bank_')) continue;
    final section = name.substring(5, name.length - 5);
    final json = jsonDecode(file.readAsStringSync()) as Json;
    for (final raw in json['questions']! as List<Object?>) {
      final question = Question.fromJson(raw! as Json, section);
      questions[question.id] = question;
    }
  }

  test('every paper uses test-pool questions only, each once', () {
    for (final paper in papers) {
      for (final useEthics in [false, true]) {
        final ids = [
          for (final section in paper.sectionsFor(useEthics: useEthics)) ...section.itemIds,
        ];
        expect(ids.toSet(), hasLength(ids.length), reason: paper.id);
        for (final id in ids) {
          expect(questions[id]?.isPractice, isFalse, reason: '${paper.id} $id');
        }
      }
    }
  });

  test('each subject has 20 mocks of 48 questions with no repeats', () {
    final catalog = Catalog.fromJson(
      jsonDecode(File('assets/data/catalog.json').readAsStringSync()) as Json,
    );
    expect(catalog.modes.map((mode) => mode.key), ['math', 'physics', 'chemistry']);
    for (final mode in catalog.modes) {
      final mine = papers.where((paper) => paper.mode == mode.key).toList();
      expect(mine, hasLength(20), reason: mode.key);
      final ids = <String>[];
      for (final paper in mine) {
        final items = [for (final section in paper.sections) ...section.itemIds];
        expect(items, hasLength(48), reason: paper.id);
        expect(paper.minutes, 60, reason: paper.id);
        ids.addAll(items);
      }
      expect(ids.toSet(), hasLength(ids.length), reason: mode.key);
    }
  });

  test('every topic has study notes', () {
    final catalog = Catalog.fromJson(
      jsonDecode(File('assets/data/catalog.json').readAsStringSync()) as Json,
    );
    for (final section in catalog.sections) {
      for (final topic in section.topics) {
        expect(topic.hasLesson, isTrue, reason: '${section.key}/${topic.key}');
      }
    }
  });

  test('every answer key points at an option', () {
    for (final question in questions.values) {
      expect(
        question.answer,
        inInclusiveRange(0, question.options.length - 1),
        reason: question.id,
      );
    }
  });
}
